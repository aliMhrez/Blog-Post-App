
db.define_table('post',
                Field('title', requires=IS_NOT_EMPTY()),
                Field('body', 'text', requires=IS_NOT_EMPTY()),
                auth.signature)

db.define_table('blog_comment',
                Field('post', 'reference post'),
                Field('body', 'text', requires=IS_NOT_EMPTY()),
                auth.signature)