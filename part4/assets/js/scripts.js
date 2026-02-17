document.addEventListener('DOMContentLoaded', () => {
    // --- UTILITIES ---
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    const token = getCookie('token');

    // --- LOGIN PAGE LOGIC ---
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                if (response.ok) {
                    const data = await response.json();
                    document.cookie = `token=${data.access_token}; path=/; max-age=3600`;
                    window.location.href = 'index.html';
                } else {
                    const errorData = await response.json();
                    alert('Login failed: ' + (errorData.message || 'Invalid credentials'));
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Is the Python server running?');
            }
        });
    }

    // --- INDEX PAGE LOGIC (LIST PLACES) ---
    const placesList = document.getElementById('places-list');
    if (placesList) {
        async function fetchPlaces() {
            try {
                const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
                    headers: token ? { 'Authorization': `Bearer ${token}` } : {}
                });
                const places = await response.json();

                placesList.innerHTML = '';
                places.forEach(place => {
                    const card = document.createElement('div');
                    card.className = 'place-card';
                    card.innerHTML = `
                        <h3>${place.title}</h3>
                        <p class="price">$${place.price} / night</p>
                        <a href="place.html?id=${place.id}" class="details-button">View Details</a>
                    `;
                    placesList.appendChild(card);
                });
            } catch (error) {
                console.error('Error fetching places:', error);
                placesList.innerHTML = '<p>Login to view available places.</p>';
            }
        }
        fetchPlaces();
    }

    // --- PLACE DETAILS PAGE LOGIC ---
    const placeDetailsContainer = document.getElementById('place-details');
    if (placeDetailsContainer && window.location.pathname.includes('place.html')) {
        const urlParams = new URLSearchParams(window.location.search);
        const placeId = urlParams.get('id');

        async function fetchPlaceDetails() {
            try {
                const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
                    headers: token ? { 'Authorization': `Bearer ${token}` } : {}
                });
                const place = await response.json();

                placeDetailsContainer.innerHTML = `
                    <h1>${place.title}</h1>
                    <div class="place-info">
                        <p><strong>Price per night:</strong> $${place.price}</p>
                        <p><strong>Description:</strong> ${place.description}</p>
                        <p><strong>Amenities:</strong> ${place.amenities ? place.amenities.map(a => a.name).join(', ') : 'None listed'}</p>
                    </div>
                    <a href="add_review.html?id=${place.id}" class="details-button" style="margin-top: 20px; display: inline-block;">Add Review</a>
                `;
            } catch (error) {
                console.error('Error:', error);
                placeDetailsContainer.innerHTML = '<p>Error loading place details.</p>';
            }
        }
        if (placeId) fetchPlaceDetails();
    }

    // --- ADD REVIEW PAGE LOGIC ---
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        if (!token) {
            alert("You must be logged in to review.");
            window.location.href = 'index.html';
        }

        const urlParams = new URLSearchParams(window.location.search);
        const placeId = urlParams.get('id');
        
        // Display Place Name
        const placeNameDisplay = document.getElementById('place-name-display');
        if (placeNameDisplay && placeId) {
             fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`)
                .then(res => res.json())
                .then(data => { placeNameDisplay.textContent = `Reviewing: ${data.title}`; });
        }

        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const text = document.getElementById('review').value;
            const rating = document.getElementById('rating').value;

            try {
                const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({
                        place_id: placeId,
                        text: text,
                        rating: parseInt(rating)
                    })
                });

                if (response.ok) {
                    alert('Review submitted successfully!');
                    window.location.href = `place.html?id=${placeId}`;
                } else {
                    const errorData = await response.json();
                    alert('Error: ' + (errorData.message || 'Failed to submit review'));
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Failed to submit review.');
            }
        });
    }
});
