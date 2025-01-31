// Przykład prostego skryptu, który wyświetla alert
document.addEventListener('DOMContentLoaded', function () {
    const buyButtons = document.querySelectorAll('.btn-buy');
    
    buyButtons.forEach(button => {
        button.addEventListener('click', function () {
            alert('Produkt dodany do koszyka!');
        });
    });
});