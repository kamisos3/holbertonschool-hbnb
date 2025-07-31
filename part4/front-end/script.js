
document.addEventListener('DOMContentLoaded', () => {
    console.log('HBnB application loaded successfully');
    
    initializePage();
    
    setupCommonEventListeners();
});

function initializePage() {
    const currentPage = window.location.pathname.split('/').pop();
    
    switch(currentPage) {
        case 'index.html':
        case '':
            initializeHomePage();
            break;
        case 'login.html':
            initializeLoginPage();
            break;
        case 'place.html':
            initializePlaceDetailsPage();
            break;
        case 'add_review.html':
            initializeAddReviewPage();
            break;
        default:
            console.log('Page specific initialization not required');
    }
}

function initializeHomePage() {
    console.log('Initializing home page...');
    
    const placeCards = document.querySelectorAll('.place-card');
    placeCards.forEach(card => {
        card.addEventListener('click', (e) => {
            if (!e.target.classList.contains('details-button')) {
                console.log('Place card clicked:', card.querySelector('h3').textContent);
            }
        });
    });
    
    addPlaceCardHoverEffects();
}


function initializeLoginPage() {
    console.log('Initializing login page...');
    
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLoginSubmit);
    }
}


function initializePlaceDetailsPage() {
    console.log('Initializing place details page...');
    
    const urlParams = new URLSearchParams(window.location.search);
    const placeId = urlParams.get('id');
    
    if (placeId) {
        console.log('Loading details for place ID:', placeId);
        loadPlaceDetails(placeId);
    }
    
    setupReviewInteractions();
}

function initializeAddReviewPage() {
    console.log('Initializing add review page...');
    
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', handleReviewSubmit);
    }
    
    setupRatingInteraction();
}

function setupCommonEventListeners() {
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            console.log('Navigation:', e.target.textContent);
        });
    });
    
    const loginButton = document.querySelector('.login-button');
    if (loginButton) {
        loginButton.addEventListener('click', (e) => {
            console.log('Login button clicked');
        });
    }
}

function handleLoginSubmit(e) {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const email = formData.get('email');
    const password = formData.get('password');
    
    console.log('Login attempt:', email);
    
    if (!email || !password) {
        alert('Please fill in all fields');
        return;
    }
    
    if (!isValidEmail(email)) {
        alert('Please enter a valid email address');
        return;
    }
    
    simulateLogin(email);
}


function handleReviewSubmit(e) {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const rating = formData.get('rating');
    const review = formData.get('review');
    const placeName = formData.get('place-name');
    
    console.log('Review submission:', { rating, review, placeName });
    
    if (!rating || !review.trim()) {
        alert('Please provide both a rating and review text');
        return;
    }
    
    if (review.trim().length < 10) {
        alert('Please provide a more detailed review (at least 10 characters)');
        return;
    }
    
    simulateReviewSubmission(rating, review, placeName);
}

function addPlaceCardHoverEffects() {
    const placeCards = document.querySelectorAll('.place-card');
    
    placeCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            console.log('Hovering over:', card.querySelector('h3').textContent);
        });
    });
}

function setupReviewInteractions() {
    const reviewCards = document.querySelectorAll('.review-card');
    
    reviewCards.forEach(card => {
        card.addEventListener('click', () => {
            const reviewer = card.querySelector('.review-user').textContent;
            console.log('Review clicked by:', reviewer);
        });
    });
}

function setupRatingInteraction() {
    const ratingSelect = document.getElementById('rating');
    
    if (ratingSelect) {
        ratingSelect.addEventListener('change', (e) => {
            console.log('Rating selected:', e.target.value);
        });
    }
}
function loadPlaceDetails(placeId) {
    console.log(`Loading place details for ID ${placeId}...`);
    
}

function simulateLogin(email) {
    console.log('Simulating login for:', email);
    
    alert('Login successful! Welcome to HBnB.');
    
    
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 1000);
}

function simulateReviewSubmission(rating, review, placeName) {
    console.log('Simulating review submission...');
    
    alert('Review submitted successfully! Thank you for your feedback.');
    
    setTimeout(() => {
        window.location.href = 'place.html';
    }, 1000);
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

const HBnBUtils = {
   
    formatPrice: function(price) {
        return `$${price}/night`;
    },
    
 
    generateStars: function(rating) {
        const stars = '★'.repeat(rating) + '☆'.repeat(5 - rating);
        return `${stars} ${rating}/5`;
    },
    
    
    truncateText: function(text, maxLength) {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength) + '...';
    }
};

window.HBnBUtils = HBnBUtils;
