$(document).ready(function() {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax( {
            url: '/store/?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return '<div class="well-game">
                                <a href="/store/${d.id}">
                                    <img class="game-img" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>'
                });
                $('.games').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});