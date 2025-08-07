<script>
    import { onMount } from 'svelte';

    let observations = [];
    let map;

    onMount(async () => {
        const response = await fetch('http://localhost:8004/observations');
        observations = await response.json();

        map = L.map('map').setView([-50, 100], 4);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '© OpenStreetMap'
        }).addTo(map);

        observations.forEach(observation => {
            if (observation.latitude && observation.longitude) {
                L.marker([observation.latitude, observation.longitude]).addTo(map)
                    .bindPopup(`<b>${observation.species_guess}</b><br>${observation.common_name}`);
            }
        });
    });
</script>

<h1>Observations</h1>

<div id="map" style="height: 400px;"></div>

{#if observations.length === 0}
    <p>Loading observations...</p>
{:else}
    <ul>
        {#each observations as observation}
            <li>
                <strong>{observation.species_guess}</strong> ({observation.common_name})
                <br />
                Observed on: {observation.observed_on}
                <br />
                Location: {observation.latitude}, {observation.longitude}
            </li>
        {/each}
    </ul>
{/if}
