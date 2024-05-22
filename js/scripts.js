        document.addEventListener('DOMContentLoaded', function() {
            const loginForm = document.getElementById('login-form');
            const loginError = document.getElementById('login-error');
            const loginBtn = document.getElementById('login-btn');
            const brightnessControl = document.getElementById('brightness');
            const settingsToggle = document.querySelector('.settings-toggle img');
            const header = document.querySelector('.header');
            const body = document.body;

            loginForm.addEventListener('submit', function(event) {
                event.preventDefault();
                const username = document.getElementById('username').value;
                const password = document.getElementById('password').value;

                if (username === 'Aluno' && password === 'Aluno') {
                    loginError.textContent = '';
                    loginError.style.display = 'none'; // Ocultar a mensagem de erro
                    const link = loginBtn.getAttribute('data-link');
                    setCookie('username', username, 30);
                    window.location.href = link;
                } else {
                    loginError.innerHTML = 'Nome de usuário ou senha incorretos<br><span style="font-size: 12px;">(Dica: use "Aluno" para ambos)</span>';
                    loginError.style.display = 'block'; // Exibir a mensagem de erro
                }
            });

            loginForm.addEventListener('keydown', function(event) {
                if (event.key === 'Enter') {
                    loginBtn.click();
                }
            });

            const cookiesAccepted = getCookie('cookiesAccepted');
            if (cookiesAccepted) {
                // Se os cookies foram aceitos, ative automaticamente a opção "Lembrar-me"
                document.getElementById('username').value = getCookie('username') || '';
            }

            var links = document.getElementsByTagName('a');
            for (var i = 0; i < links.length; i++) {
                var href = links[i].getAttribute('href');
                if (href && href.endsWith('.html')) {
                    links[i].setAttribute('href', href.slice(0, -5));
                }
            }

            const cookieModal = new bootstrap.Modal(document.getElementById('cookieModal'));
            const acceptCookiesBtn = document.getElementById('accept-cookies');

            // Mostrar modal de cookies ao carregar a página
            if (!cookiesAccepted) {
                cookieModal.show();
            }

            acceptCookiesBtn.addEventListener('click', function() {
                cookieModal.hide();
                setCookie('cookiesAccepted', 'true', 30);
            });

            // Controle de brilho
            brightnessControl.addEventListener('input', function() {
                body.style.filter = `brightness(${brightnessControl.value})`;
            });

            // Alternar menu de configurações
            settingsToggle.addEventListener('click', function() {
                header.classList.toggle('expanded');
            });

            function setCookie(name, value, days) {
                var expires = "";
                if (days) {
                    var date = new Date();
                    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                    expires = "; expires=" + date.toUTCString();
                }
                document.cookie = name + "=" + (value || "") + expires + "; path=/";
            }

            function getCookie(name) {
                const nameEQ = name + "=";
                const ca = document.cookie.split(';');
                for(let i = 0; i < ca.length; i++) {
                    let c = ca[i].trim();
                    if (c.indexOf(nameEQ) === 0) {
                        return c.substring(nameEQ.length, c.length);
                    }
                }
                return null;
            }
        });
