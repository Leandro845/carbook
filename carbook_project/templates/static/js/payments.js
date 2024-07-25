// Replace with your own publishable API key from Stripe
const stripe = Stripe("{{ STRIPE_PUBLIC_KEY }}");

let elements;

// Initialize Stripe Elements and fetch the PaymentIntent client secret
async function initialize() {
  const response = await fetch("{% url 'payment_intent' car.id %}", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ price: document.getElementById('price').value }),
  });

  const { clientSecret } = await response.json();

  const appearance = {
    theme: 'stripe',
  };
  elements = stripe.elements({ appearance });

  const paymentElement = elements.create("payment");
  paymentElement.mount("#payment-element");
}

// Handle form submission and confirm the payment
async function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);

  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: {
      return_url: `http://127.0.0.1:8000/{% url 'success' %}`,
    },
  });

  if (error) {
    showMessage(error.message);
  } else {
    showMessage("An unexpected error occurred.");
  }

  setLoading(false);
}

// Check the payment status on page load
async function checkStatus() {
  const clientSecret = new URLSearchParams(window.location.search).get("payment_intent_client_secret");

  if (!clientSecret) {
    return;
  }

  const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

  switch (paymentIntent.status) {
    case "succeeded":
      showMessage("Payment succeeded!");
      break;
    case "processing":
      showMessage("Your payment is processing.");
      break;
    case "requires_payment_method":
      showMessage("Your payment was not successful, please try again.");
      break;
    default:
      showMessage("Something went wrong.");
      break;
  }
}

// Show a message to the user
function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");

  messageContainer.classList.remove("hidden");
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add("hidden");
    messageContainer.textContent = "";
  }, 4000);
}

// Show a spinner during loading
function setLoading(isLoading) {
  if (isLoading) {
    document.querySelector("#submit").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}

// Initialize the Stripe Elements and check payment status on page load
initialize();
checkStatus();

// Attach the handleSubmit function to the form submit event
document.querySelector("#payment-form").addEventListener("submit", handleSubmit);
