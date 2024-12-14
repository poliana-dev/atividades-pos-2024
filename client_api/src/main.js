import { fetchAlbuns, fetchAlbunsDetails, fetchArtistas, fetchArtistasDetails, fetchMusicas } from "./wrapper";

// Carrega a lista de artistas e popula o acordeão
export async function loadArtistas() {
    try {
        const artistas = await fetchArtistas();
        const artistasAccordion = document.getElementById('artistas-accordion');
        artistasAccordion.innerHTML = ''; // Limpa o acordeão

        artistas.forEach((artista, index) => {
            const accordionItem = document.createElement('div');
            accordionItem.className = 'accordion-item';

            accordionItem.innerHTML = `
                <h2 class="accordion-header" id="heading-${index}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-${index}" aria-expanded="false" aria-controls="collapse-${index}">
                        ${artista.nome}
                    </button>
                </h2>
                <div id="collapse-${index}" class="accordion-collapse collapse" aria-labelledby="heading-${index}" data-bs-parent="#artistas-accordion">
                    <div class="accordion-body" id="artista-details-${index}">
                        <div class="text-center">Carregando detalhes...</div>
                    </div>
                </div>
            `;

            artistasAccordion.appendChild(accordionItem);

            // Adiciona evento para carregar detalhes ao expandir
            accordionItem.querySelector('.accordion-button').addEventListener('click', () => {
                const detailsElement = document.getElementById(`artista-details-${index}`);
                if (!detailsElement.classList.contains('loaded')) {
                    loadArtistaDetails(artista.id, index);
                }
            });
        });
    } catch (error) {
        console.error('Erro ao buscar os artistas:', error);
        alert('Não foi possível carregar os artistas.');
    }
}

// Carrega os detalhes de um artista
async function loadArtistaDetails(artista_id, index) {
    try {
        const artista = await fetchArtistasDetails(artista_id);
        const detailsElement = document.getElementById(`artista-details-${index}`);

        detailsElement.innerHTML = `
            <p><strong>Nome:</strong> ${artista.nome}</p>
            <p><strong>Local:</strong> ${artista.local}</p>
            <p><strong>Ano de Criação:</strong> ${artista.ano_criacao}</p>
    
        `;
        detailsElement.classList.add('loaded');

    } catch (error) {
        console.error('Erro ao carregar os detalhes do artista:', error);
        alert('Não foi possível carregar os detalhes do artista.');
    }
}


// Adicione os elementos do DOM
document.querySelector('#app').innerHTML = `
    <div class="d-grid gap-2 col-6 mx-auto">
        <button id="load-artistas-btn" class="btn btn-primary btn-lg">Carregar Artistas</button>
    </div>
    <div class="accordion mt-4" id="artistas-accordion"></div>
    ;`

// Adicione os eventos de clique para carregar os dados
document.getElementById('load-artistas-btn').addEventListener('click',loadArtistas);
