import os
from app import app

def main():
    app.run(host='0.0.0.0', debug='False')

if __name__=="__main__":
    main()
    
