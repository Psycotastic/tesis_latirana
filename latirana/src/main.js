document.addEventListener('DOMContentLoaded', function () {
    const postsBox = document.getElementById('posts-box');
    const spinnerBox = document.getElementById('spinner-box');
    const loadBtn = document.getElementById('load-more');
    const noMorebox = document.getElementById('no-more-box');
    let visible = 6;

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
                    postsBox.innerHTML += "<div class='post' style='background-image: url(media\/" + post.image + ")'>" +
                                "<a href='javascript:void(0) class='photo-modal' data-guild='" + post.guild + "' " +
                                "data-image='" + post.image +"data-performance='" + post.performance + "' " +
                                "data-year='"+ post.year + "' data-costume='" + post.costume + "' " +
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

    handleGetData();

    loadBtn.addEventListener('click', ()=>{
        visible += 3;
        handleGetData();
    })

    /*Descargar ficha*/
    $('#download-pdf').click(function() {
        let source = document.getElementById("photoModal");
        console.log("PASE");
        let doc = new jsPDF(source);
        doc.fromHtml();
        doc.print();

    });

});