<script>
    import { onMount } from 'svelte';

    let observations = [];

    onMount(async () => {
        const response = await fetch('http://localhost:8004/observations');
        observations = await response.json();
    });
</script>

<h1>Manage Observations</h1>

<table>
    <thead>
        <tr>
            <th>Species Guess</th>
            <th>Observed On</th>
            <th>Location</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {#each observations as observation}
            <tr>
                <td>{observation.species_guess}</td>
                <td>{observation.observed_on}</td>
                <td>{observation.latitude}, {observation.longitude}</td>
                <td>
                    <a href="/admin/observations/{observation.observation_id}">Edit</a>
                </td>
            </tr>
        {/each}
    </tbody>
</table>
