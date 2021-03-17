from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def login():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    list_jobs = []
    for job in db_sess.query(Jobs).all():
        list_jobs.append({'id': job.id, 'title': job.job, 'leader': f'{job.user.name} {job.user.surname}',
                          'duration': job.work_size, 'list': job.collaborators, 'finish': job.is_finished})
    return render_template('table.html', data=list_jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
