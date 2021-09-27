
var updateBtns = document.getElementsByClassName('update-cart')

    var user = '{{request.user}}'
    for(i = 0; i < updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function () {
            var productid = this.dataset.product
            var action = this.dataset.action
            console.log('productid:', productid, 'Action:', action)
            console.log("USER:", user)

            if (user === 'AnonymousUser'){
                console.log('Unknown User')
            }else {
                updateUserOrder(productid, action)
            }
        })
    }


function updateUserOrder(productid, action){
        console.log('user not logged in')


        var url = '/update_item/'

        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'productid': productid, 'action': action})
        })
        .then((response) =>{
            return response.json()
        })
        .then((data)=>{
            console.log('data:', data)
        });
    }