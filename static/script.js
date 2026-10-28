async function generateRecipe() {

    const ingredients =
        document.getElementById("ingredients").value;

    const basket = document.getElementById("basket");
    const foodContainer =
        document.getElementById("food-container");

    const card = document.getElementById("recipeCard");
    const recipeText =
        document.getElementById("recipeText");

    recipeText.innerHTML = "";

    // create falling foods
    const items = ingredients.split(",");

    items.forEach((item, i) => {
        const food = document.createElement("div");
        food.className = "food";
        food.innerText = item.trim();
        food.style.left = (40 + i*60) + "px";
        food.style.top = "0px";
        foodContainer.appendChild(food);

        setTimeout(()=>food.remove(),1000);
    });

    basket.classList.add("active");

    // call backend
    const response = await fetch("/generate_recipe",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({ingredients})
    });

    const data = await response.json();

    // flip card
    setTimeout(()=>{
        card.classList.add("flip");
        typeWriter(data.recipe, recipeText);
    },1200);
}


// typing animation
function typeWriter(text, element){
    let i=0;
    function type(){
        if(i<text.length){
            element.innerHTML+=text.charAt(i);
            i++;
            setTimeout(type,15);
        }
    }
    type();
}