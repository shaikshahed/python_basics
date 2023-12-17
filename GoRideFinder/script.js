async function registerUser() {
    const form = document.getElementById("registrationForm");
    const username = form.elements.username.value;
    const email = form.elements.email.value;
    const password = form.elements.password.value;

    const response = await fetch('http://127.0.0.1:8000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            email: email,
            password: password,
        }),
    });

    const result = await response.json();
    alert(result.message);
}
