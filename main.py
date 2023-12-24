import os
import typer, click
import requests
from PIL import Image
from cropper import crop
from fspy import FlareSolverr
from typing import Optional


class NaturalOrderGroup(click.Group):
  def list_commands(self, ctx):
    return self.commands.keys()


app = typer.Typer(cls=NaturalOrderGroup, add_completion=False)
              
@app.command()
def main(url):
  # try:
    solver = FlareSolverr(host='0.0.0.0', port=8191, http_schema='http')
    # print(locals())
    new_session = solver.create_session(session_id='ifunny')
    list_session = solver.sessions
    if new_session.status == 'error':
      print('error occured in session')
      solver.destroy_session(new_session.session)
      SystemExit
    else:
      pass
    print(list_session)
    solver.request_get(url=url, session=new_session.session)

  # except Exception as e:
    # solver.destroy_session(new_session.session)
    # SystemExit
if __name__ == "__main__":
  typer.run(main)
  