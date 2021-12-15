describe('Registration and Login for App', () => {
    it('Creates a new user', () => {
        cy.visit('http://localhost:3000/register')

        cy.get('input#register_firstname')
        .type('Titi')

        cy.get('input#register_lastname')
            .type('Adebisi')

        cy.get('input#register_username')
            .type('titi')

        cy.get('input#register_email')
            .type('titi@test.com')

        cy.get('input#register_password')
            .type('titi01')

        cy.contains('Sign up')
            .click()

    })
})

