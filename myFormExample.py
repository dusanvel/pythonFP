from flask import Flask, render_template, request, flash,redirect, url_for
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   
   if request.method == 'POST':
      if form.validate() == False:
         print "!! All fields are required!!"
         flash('All fields are required.')

         return render_template('contact.html', form = form)
      else:
         print form.name.data
         print form.language.data
         return render_template('success.html', form=form)

        
   elif request.method == 'GET':
         return render_template('contact.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8090)
