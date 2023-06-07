from flask import Flask,render_template,request

FAI=Flask(__name__)

@FAI.route('/HtmlForm',methods=['GET','POST'])
def HtmlForm():
    if request.method=='POST':
        form_data=request.form
        print(form_data)
        return request.form['na']

    return render_template('HtmlForm.html')

@FAI.route('/Greshma')
def Greshma():
    return 'Greeshma papa'

if __name__=='__main__':
    FAI.run(debug=True)