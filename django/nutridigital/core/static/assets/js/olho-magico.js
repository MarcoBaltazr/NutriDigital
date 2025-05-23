const passwordInput = document.getElementById('password');
const togglePassword = document.getElementById('togglePassword')

togglePassword.addEventListener('click', function(){
    const isVisible = passwordInput.type === 'text';

    passwordInput.type = isVisible ? 'password' : 'text';
    togglePassword.type = isVisible ? '/assets/image/eye-off.svg' : '/assets/image/eye.svg'; 
});

const confirmPasswordInput = document.getElementById('confirmPassword');
const toggleConfirmPassword = document.getElementById('toggleConfirmPassword')

toggleConfirmPassword.addEventListener('click', function(){
    const isVisible = confirmPasswordInput.type === 'text';

    confirmPasswordInput.type = isVisible ? 'password' : 'text';
    toggleConfirmPassword.type = isVisible ? '/assets/image/eye-off.svg' : '/assets/image/eye.svg'; 
});
