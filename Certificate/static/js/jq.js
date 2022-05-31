// navbars = document.querySelector(".degistirecem").querySelectorAll("a");
// console.log(navbars);
//
// navbars.forEach(element => {
//
//
//     element.addEventListener("click", function () {
//         navbars.forEach(nav => nav.classList.remove("Active"));
//         this.classList.add('Active');
//     })
// })


const currentLocation = location.href;

// const menuItem = document.querySelectorAll('a');
const menuItem = document.querySelector(".degistirecem").querySelectorAll("a");
const menuLenth= menuItem.length;
for (let i = 0; i<menuLenth; i++){
    if (menuItem[i].href === currentLocation){
        menuItem[i].className = "Active"
    }
}

