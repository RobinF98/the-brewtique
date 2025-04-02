let stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
let client_secret= $('#id_client_secret').text().slice(1,-1);
let stripe = Stripe(stripe_public_key);
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