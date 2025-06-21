let stripePublicKey = $('#id_stripe_public_key').text().slice(1,-1);
let clientSecret= $('#id_client_secret').text().slice(1,-1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style =  {
    base: {
        iconColor: '#c4f0ff',
        color: '#000',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
        color: '#fce883',
        },
        '::placeholder': {
        color: '#aab7c4',
        },
    },
    invalid: {
        iconColor: '#dc3545',
        color: '#dc3545',
    },
};
let card = elements.create('card', {style: style} );
card.mount('#card-element')

// Handling of validation errors on card element:
card.addEventListener('change', function (event){
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `<span class="icon" role="alert"><i class="fas fa-times"></i> </span><span>${event.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        $(errorDiv).textContent = '';
    }
});

// Handle submit
let form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            let errorDiv = document.getElementById('card-errors');
            let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});