export async function loadWars() {
    try {
        const url = 'https://swapi.dev/api/people/';
        const response = await fetch(url); 
        const data = await response.json(); 
        const people = data.results;

        people.forEach((person, index) => {

            const accordionItem = document.createElement('div');
            accordionItem.className = 'accordion-item';


            
            peopleAccordion.appendChild(accordionItem);
        });
       

    } catch (error) {
        console.error('Erro ao buscar os personagens:', error);
        alert('Não foi possível carregar os personagens.');
    }
}


