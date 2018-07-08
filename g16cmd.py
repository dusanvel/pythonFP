@app.route('/g16_cmd', methods = ['GET', 'POST'])
def g16_cmd():
    from cmd_get_diag import cmd_Get_Diag
    form = SubmitForm()

    if request.method == 'POST':
        form_output = cmd_Get_Diag()
        return render_template('g16success.html', output = form_output)

    elif request.method == 'GET':
        return render_template('g16CMD.html', form = form)
cmd_Get_Diag()
