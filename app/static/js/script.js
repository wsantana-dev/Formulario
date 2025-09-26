function validarFormulario() {
    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();

    if (!nome || !email || !mensagem) {
        alert('Por favor, preencha todos os campos.');
        return false;
    }

    // Validação de email
    const emailValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    if (!emailValido) {
        alert('Digite um email válido.');
        return false;
    }

    return true;
}


