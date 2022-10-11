
# FlaskIntroduction

This repo has been updated to work with `Python v3.8` and up.

## How To Run

1. Install `virtualenv` (assuming you are on Windows):
```
$ py -3 -m venv venv
```

2. Open a terminal in the project directory directory and run:
```
$ venv\Scripts\activate
```

4. Then install the dependencies:
```
$ (venv) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (venv) python run.py
```

This server will start on port 5000 by default. You can change this in `run.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
