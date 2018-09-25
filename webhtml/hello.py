#! /usr/local/bin python
# ! -*-coding:utf-8 -*-
# ! time      :9/25/18 14:59
# ! @Auther   : whitek
# ! @File     :hello.py
# ! code is far away from bugs with the god animal protecting i love animals.They taste delicious.

import web

import model

# URL映射

urls = (
    '/', 'Index',
    '/view/(/d+)', 'View',
    '/new', 'New',
    '/delete/(/d+)', 'Delete',
    '/edit/(/d+)', 'Edit',
    '/login', 'Login',
    '/logout', 'Logout',
)

app = web.application(urls, globals())

# 模板公共变量
t_globals = {
    'datestr': web.datestr,
    'cookie': web.cookies,
}

# 指定模板目录
render = web.template.render('templates', base='base', globals=t_globals)

# 创建登录表单
login = web.form.Form(
    web.form.Textarea('username'),
    web.form.Password('password'),
    web.form.Button('login')
)

# 首页类

class Index():
    def GET(self):
        login_form = login()
        posts = model.get_posts()
        return render.index(posts, login_form)

    def POST(self):
        login_form = login()
        if login_form.validates():
            if login_form.d.username == 'admin' and login_form.d.password == 'admin':
                web.setcookie('username', login_form.d.username)
        raise web.seeother('/')

# 查看文章类
class View():
    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)


# 新建文章类
class New():
    form = web.form.Form(
        web.form.Textarea('title', web.form.notnull, size=30, description='Post title:'),
        web.form.Textarea('content', web.form.notnull, rows=30, cols=80, description='Post content: '),
        web.form.Button('Post entry'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new()
        model.new_post(form.d.title, form.d.content)
        raise web.seeother('/')

# 删除文章类
class Delete():
    def POST(self, id):
        model.del_port(int(id))
        raise web.seeother('/')

# 编辑文章类
class Edit():
    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)
    def POST(self, id):
        form = New.form()
        post = model.get_post(int(id))
        if not form.validates():
            return  render.edit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/')

# 退出登录
class Logout():
    def GET(self):
        web.setcookie('username', '', expires=-1)
        raise web.seeother('/')

# 定义404错误
def notfound():
    return web.notfound('sorry, the page loss!')

app.notfound = notfound

if __name__ == '__main__':
    app.run()
