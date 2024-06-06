document.addEventListener('DOMContentLoaded', function() {
    const cartIcon = document.querySelector('.cart-icon');
    const cartContent = document.querySelector('.cart-content');
    const cartProducts = document.querySelector('.cart-products');
    const cartTotalPrice = document.querySelector('.cart-total-price');
    const cartCheckoutButton = document.querySelector('.cart-checkout');
    let cartVisible = false;
    const productsInCart = [];

    const addToCartButtons = document.getElementsByClassName('add-to-cart-button');
    Array.from(addToCartButtons).forEach(function(addToCartButton) {
        addProductToCart(addToCartButton);
    });

    function addProductToCart(button) {
        button.addEventListener('click', function() {
            console.log('Dodano do koszyka!');
            const productName = button.dataset.productName;
            const productPrice = parseFloat(button.dataset.productPrice);
            productsInCart.push({ name: productName, price: productPrice });

            renderCartProducts();
            updateCartCount();
            calculateTotalPrice();

            if (!cartVisible) {
                cartContent.classList.add('show');
                cartVisible = true;
            }
        });
    }

    function renderCartProducts() {
        cartProducts.innerHTML = '';
        productsInCart.forEach(function(product) {
            const listItem = document.createElement('li');
            listItem.textContent = `${product.name} - ${product.price}zł`;

            const removeButton = document.createElement('button');
            removeButton.innerHTML = '<i class="fas fa-times"></i>';
            removeButton.addEventListener('click', function() {
                productsInCart.splice(productsInCart.indexOf(product), 1);
                cartProducts.removeChild(listItem);
                updateCartCount();
                calculateTotalPrice();
            });

            listItem.appendChild(removeButton);
            cartProducts.appendChild(listItem);
        });
    }

    function updateCartCount() {
        const cartCount = document.getElementById('cart-count');
        console.log(cartCount); // Dodaj to logowanie
        cartCount.textContent = productsInCart.length;
        
        if(productsInCart.length > 0) {
            document.querySelector('.cart-count').classList.add('visible');
        } else {
            document.querySelector('.cart-count').classList.remove('visible');
        }
    }

    function calculateTotalPrice() {
    let totalPrice = 0;
    productsInCart.forEach(function(product) {
        totalPrice += product.price;
    });
    cartTotalPrice.textContent = 'Suma: ' + totalPrice + 'zł';
}

    

    cartContent.addEventListener('click', function() {
        cartContent.classList.remove('show');
        cartVisible = false;
    });

    cartIcon.addEventListener('click', function() {
        cartContent.classList.toggle('show');
        cartVisible = !cartVisible;
    });

    cartCheckoutButton.addEventListener('click', function() {
        alert('Zamówienie zostało przypisane do numeru #12345');
    });

    console.log('Scripts.js is connected!');
});