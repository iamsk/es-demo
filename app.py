# -*- coding: utf-8 -*-

from bottle import route, template, run, debug, redirect
from data import Data
from pyes import ES, TextQuery, HighLighter, Search, BoolQuery


@route('/init')
def init():
    conn = ES('127.0.0.1:9200')
    try:
        conn.delete_index("zhihu")
    except:
        pass
    conn.create_index("zhihu")
    mapping = {
        u'id': {'store': 'yes',
                'type': u'integer'},
        u'link': {'store': 'yes',
                  'type': u'string'},
        u'title': {'boost': 1.0,
                   'index': 'analyzed',
                   'store': 'yes',
                   'type': u'string'},
    }
    conn.put_mapping("answer", {'properties': mapping}, ["zhihu"])
    for item in Data().getData():
        conn.index(item, "zhihu", "answer", item['id'])
    conn.refresh(["zhihu"])
    return redirect('/list')


@route('/list')
def list():
    data = Data()
    results = data.getData()
    return template('results.html', list=results, count=len(results))


@route('/search')
@route('/search/<searchkey>')
def search(searchkey=u"电影"):
    conn = ES('127.0.0.1:9200')
    # TextQuery会对searchkey进行分词
    qtitle = TextQuery("title", searchkey)
    h = HighLighter(['<b>'], ['</b>'], fragment_size=500)
    # 多字段搜索(must=>and,should=>or)，高亮，结果截取（分页），排序
    q = Search(BoolQuery(should=[qtitle]), highlight=h, start=0, size=3,
               sort={'id': {'order': 'asc'}})
    q.add_highlight("title")
    results = conn.search(q, "zhihu", "answer")
    list = []
    for r in results:
        if("title" in r._meta.highlight):
            r['title'] = r._meta.highlight[u"title"][0]
        list.append(r)
    return template('results.html', list=list, count=results.total)

debug(True)
run(host='localhost', port=9527, reloader=True)
