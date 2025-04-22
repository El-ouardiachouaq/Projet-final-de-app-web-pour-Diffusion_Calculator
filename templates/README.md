# All templates corrected for CSRF: Template Fragments

## **login.html** and **register.html**
<!-- Example for login.html, same for register.html -->
<form method="POST" action="{{ url_for('auth.login') }}">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
    <!-- rest of your fields -->
</form>

## **calculator.html**
<!-- Inside the <form> tag -->
<form method="POST" action="{{ url_for('main.calculate') }}">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
    <!-- rest of your fields -->
</form>

## **reset_password.html**
<form method="post" class="mt-4">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
    <!-- rest of your fields -->
</form>

## **reset_password_request.html**
<form method="post" action="{{ url_for('auth.reset_password_request') }}" class="mt-4">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
    <!-- rest of your fields -->
</form>