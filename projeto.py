from selenium import webdriver
import time

class TestAutomation:
    def __init__(self):
        # Configurar o WebDriver (certifique-se de ter o webdriver correspondente no seu PATH ou forneça o caminho)
        self.driver = webdriver.Chrome()

    def run_test(self):
        try:
            # Abrir a página
            self.driver.get("https://practice.automationtesting.in/")

            # Aguardar um curto período de tempo para garantir que a página seja totalmente carregada
            time.sleep(2)

            # Clicar no link "My Account" no menu superior
            my_account_link = self.driver.find_element_by_link_text("My Account")
            my_account_link.click()

            # Aguardar um pouco para a página "My Account" carregar completamente
            time.sleep(2)

            # Preencher os campos "Email address" e "Password" e clicar em Register
            email_input = self.driver.find_element_by_id("reg_email")
            email_input.send_keys("seu_email@example.com")

            password_input = self.driver.find_element_by_id("reg_password")
            password_input.send_keys("sua_senha")

            register_button = self.driver.find_element_by_name("register")
            register_button.click()

            # Aguardar um pouco para a página de registro ser processada
            time.sleep(5)

            # Adicionar verificações adicionais, por exemplo, verificar se o login foi bem-sucedido
            # (exemplo: verificar a presença de um elemento específico após o login)
            success_message = self.driver.find_element_by_css_selector(".woocommerce-MyAccount-content p:first-child")
            if "Thank you for registering!" in success_message.text:
                print("Registro bem-sucedido!")
            else:
                print("Erro durante o registro.")

        except Exception as e:
            print(f"Erro durante o teste: {e}")

        finally:
            # Fechar o navegador ao final do teste
            self.driver.quit()

# Instanciar a classe e executar o teste
test = TestAutomation()
test.run_test()
