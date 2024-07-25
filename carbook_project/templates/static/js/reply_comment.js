/*
document.addEventListener('DOMContentLoaded', function () {
    // Event listener para todos os links "Reply"
    document.querySelectorAll('.reply').forEach(function (replyLink) {
        replyLink.addEventListener('click', function (event) {
            event.preventDefault();
            var commentId = this.getAttribute('data-comment-id');
            var form = document.getElementById('reply-form');
            var parentInput = document.getElementById('parent_id');
            parentInput.value = commentId;

            var commentElement = this.closest('.comment');
            commentElement.appendChild(form);
            form.style.display = 'block';
            
            form.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    document.addEventListener('click', function (event) {
        var replyForm = document.getElementById('reply-form');
        var isClickInsideForm = replyForm.contains(event.target);
        var isReplyLink = event.target.classList.contains('reply');

        if (!isClickInsideForm && !isReplyLink) {
            replyForm.style.display = 'none';
        }
    });
}); */

/*
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.reply').forEach(function (replyLink) {
        replyLink.addEventListener('click', function (event) {
            event.preventDefault();
            var commentId = this.getAttribute('data-comment-id');
            var form = document.getElementById('reply-form');
            var parentInput = document.getElementById('parent_id');
            parentInput.value = commentId;

            var commentElement = this.closest('.comment');
            var childrenList = commentElement.querySelector('.children');

            if (!childrenList) {
                childrenList = document.createElement('ul');
                childrenList.classList.add('children');
                commentElement.appendChild(childrenList);
            }

            var replyListItem = document.createElement('li');
            replyListItem.classList.add('comment');
            childrenList.appendChild(replyListItem);
            replyListItem.appendChild(form);
            form.style.display = 'block';
            form.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    // Event listener para fechar a caixa de comentários ao clicar fora dela
    document.addEventListener('click', function (event) {
        var replyForm = document.getElementById('reply-form');
        var isClickInsideForm = replyForm.contains(event.target);
        var isReplyLink = event.target.classList.contains('reply');

        if (!isClickInsideForm && !isReplyLink) {
            replyForm.style.display = 'none';
        }
    });
}); */

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.reply').forEach(function (replyLink) {
        replyLink.addEventListener('click', function (event) {
            event.preventDefault();
            var commentId = this.getAttribute('data-comment-id');
            var form = document.getElementById('reply-form');
            var parentInput = document.getElementById('parent_id');
            parentInput.value = commentId;

            // Encontrar o comentário pai para inserir a resposta
            var commentElement = this.closest('.comment');
            var childrenList = commentElement.querySelector('.children');

            // Se não houver lista de respostas, cria uma
            if (!childrenList) {
                childrenList = document.createElement('ul');
                childrenList.classList.add('children');
                commentElement.appendChild(childrenList);
            }

            // Cria um item de lista para a resposta
            var replyListItem = document.createElement('li');
            replyListItem.classList.add('comment');
            childrenList.appendChild(replyListItem);
            replyListItem.appendChild(form);
            form.style.display = 'block';
            form.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    // Event listener para fechar a caixa de comentários ao clicar fora dela
    document.addEventListener('click', function (event) {
        var replyForm = document.getElementById('reply-form');
        var isClickInsideForm = replyForm.contains(event.target);
        var isReplyLink = event.target.classList.contains('reply');

        if (!isClickInsideForm && !isReplyLink) {
            replyForm.style.display = 'none';
        }
    });
});


