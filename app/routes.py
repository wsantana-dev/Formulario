from flask import Blueprint, render_template, request, flash

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')

        if not nome or not email or not mensagem:
            flash('Todos os campos são obrigatórios!', 'erro')
        else:
            # 👇 Aqui simulamos o envio — sem e-mail
            print(f'Nova mensagem recebida:\nNome: {nome}\nEmail: {email}\nMensagem: {mensagem}\n')

            # ✅ Mensagem de sucesso
            flash('Cadastro enviado com sucesso!', 'sucesso')

        return render_template('formulario.html', nome=nome, email=email, mensagem=mensagem)

    return render_template('formulario.html')

