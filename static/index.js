console.log("hello")


const form=document.querySelector('#form');

const URL="http://localhost:5000/"


const submitForm=(event)=>{
    event.preventDefault();

    const formData= new FormData(form);

    const requestOptions={
        method:"POST",
        headers:{
            "content-type":"application/json"
        },
        body:JSON.stringify({searchterm:formData.get('search')})
    }

    console.log(requestOptions);


    fetch(URL,requestOptions)
    .then(response=>response.json())
    .then(data=>{
        
        console.log(data)
        form.reset()
    })
    .catch(err=>console.log(err))

    
}


form.addEventListener('submit',submitForm);