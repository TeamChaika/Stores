document.getElementById('searchInput').addEventListener('input', function() {
    let filter = this.value.toLowerCase();
    let list = document.getElementById('list');
    let items = list.querySelectorAll('li');

    items.forEach(function(item) {
        let text = item.textContent.toLowerCase();
        if (text.indexOf(filter) != -1) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
});

