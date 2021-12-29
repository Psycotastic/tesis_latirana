document.addEventListener('DOMContentLoaded', function () {
    const postsBox = document.getElementById('posts-box');
    const spinnerBox = document.getElementById('spinner-box');
    const loadBtn = document.getElementById('load-more');
    const noMorebox = document.getElementById('no-more-box');
    const loadSeachBtn = document.getElementById('load-more-search');
    const entriesBox = document.getElementById('entry-box');
    //const uploadForm = document.getElementById('uploadForm');

    const margins = {
        top: 80,
        bottom: 60,
        left: 40,
        width: 522
    };
    let visible = 10;
    let visibleSearch = 10;

    const handleGetData = () => {
        spinnerBox.classList.remove('not-visible')
        loadBtn.classList.add('not-visible');
        $.ajax({
            type: 'GET',
            url: `posts/${visible}/`,
            success: function(response){
                const data = response.data;
                max_size = response.max
                data.map(post=>{
                    image_url = "media/" + post.image;
                    postsBox.innerHTML += "<div class='post' style='background-image: url("+image_url+")'>" +
                                "<a href='javascript:void(0)' class='photo-modal' data-guild='" + post.guild + "' " +
                                "data-image='" + post.image +"' data-performance='" + post.performance + "' " +
                                "data-year='"+ post.year + "' data-costume='" + post.costume + "' " +
                                "data-character='"+ post.character + "' data-author='" + post.author + "' " +
                                "data-model='"+ post.model + "' data-apertureValue='" + post.apertureValue + "' " +
                                "data-exposureTime='"+ post.exposureTime + "' data-focalLength='" + post.focalLength + "' " +
                                "data-id='" + post.id + "' data-iso='" + post.iso + "' " + 
                                "onclick='displayModal(this)'>" +
                                "<div class='post_tag'><div><p>" + post.guild + "</p></div></div></a></div>"
                });
                if(max_size) {
                    loadBtn.classList.add('not-visible');
                    noMorebox.classList.remove('not-visible');
                }else{
                    loadBtn.classList.remove('not-visible');
                }
            },
            error: function(error){
                console.log(error);
            },
            complete: function(){
                spinnerBox.classList.add('not-visible')
            }
        });
    }

    const handleGetEntries = () => {
        $.ajax({
            type: 'GET',
            url: '/entries/',
            success: function(response) {
                const data = response.data;
                const json = JSON.parse(data);
                json.map(entry=>{
                    entriesBox.innerHTML += "<div class='entry'>" +
                                            "<h3>" + entry.society + "</h3>" + 
                                            "<a href='/entry/"+ entry.id +"'>Leer más...</a>" + "</div>";
                });
            },
            error: function(error) {

            },
            complete: function() {

            }
        });
    }

    if(window.location.pathname === "/") {
        handleGetData();
        loadBtn.addEventListener('click', ()=>{
            visible += 10;
            handleGetData();
        })
    }

    if(window.location.pathname === "/guilds/") {
        handleGetEntries();
    }

    
    if(window.location.pathname === "/search_results/") {
        loadSeachBtn.addEventListener('click', ()=>{
            visibleSearch += 6;
            handleGetDataSearch();
        })
    }

    
    
    const handleGetDataSearch = () => {
        spinnerBox.classList.remove('not-visible')
        loadSeachBtn.classList.add('not-visible');
        let input = document.getElementById('search_input').value
        $.ajax({
            type: 'GET',
            url: `/search/${input}/posts/${visibleSearch}/`,
            success: function(response){
                const data = response.data;
                max_size = response.max
                const json = JSON.parse(data)
                console.log(json)
                json.map(post=>{
                    image_url = "media/" + post.image;
                    postsBox.innerHTML += "<div class='post' style='background-image: url("+image_url+")'>" +
                                "<a href='javascript:void(0)' class='photo-modal' data-guild='" + post.guild + "' " +
                                "data-image='" + post.image +"' data-performance='" + post.performance + "' " +
                                "data-year='"+ post.year + "' data-costume='" + post.costume + "' " +
                                "data-character='"+ post.character + "' data-author='" + post.author + "' " +
                                "data-model='"+ post.model + "' data-apertureValue='" + post.apertureValue + "' " +
                                "data-exposureTime='"+ post.exposureTime + "' data-focalLength='" + post.focalLength + "' " +
                                "data-id='" + post.id + "' data-iso='" + post.iso + "' " + 
                                "onclick='displayModal(this)'>" +
                                "<div class='post_tag'><div><p>" + post.guild + "</p></div></div></a></div>"
                });
                if(max_size) {
                    loadSeachBtn.classList.add('not-visible');
                    noMorebox.classList.remove('not-visible');
                }else{
                    loadSeachBtn.classList.remove('not-visible');
                }
            },
            error: function(error){
                console.log(error);
            },
            complete: function(){
                spinnerBox.classList.add('not-visible')
            }
        });
    }

    /*Descargar ficha*/
    $('#download-pdf').click(function() {
        $(".ignorePDF").hide();
        //let source  = $('#photoModal').html();
        print();
        $(".ignorePDF").show();
    });

    $('#searchForm').submit(function() {
        let searchTerms = $('#buscar').val().trim();
        if (!searchTerms.replace(/\s/g, '').length) {
            if($(".alert").is(":hidden")) { 
                $(".alert").slideDown();
             }
            return false;
        }
        else {
            $('#buscar').val(searchTerms);
        }
    });

    $(".alert").click(function() {
        $(".alert").slideUp();
    });
    
});