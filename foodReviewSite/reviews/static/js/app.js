
window.addEventListener('DOMContentLoaded', (event) => {

    if(document.getElementById('review')){
        document.getElementById('review').onclick=()=>{
            document.querySelectorAll('#text_review').forEach(element=>{
                element.style.visibility="visible"; 
            })    
        };
    }
    
});


