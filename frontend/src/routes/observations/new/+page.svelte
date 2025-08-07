<script>
    import { onMount } from 'svelte';
    import { supabase } from '$lib/supabaseClient';

    let voyages = [];
    let users = [];
    let species_guess = '';
    let common_name = '';
    let notes = '';
    let selectedVoyage = '';
    let selectedUser = '';
    let photo;

    onMount(async () => {
        const { data: voyagesData } = await fetch('http://localhost:8004/voyages').then(res => res.json());
        voyages = voyagesData;

        const { data: usersData } = await fetch('http://localhost:8004/users').then(res => res.json());
        users = usersData;
    });

    async function handleSubmit() {
        let photo_path = null;
        if (photo) {
            const { data, error } = await supabase.storage
                .from('photo-uploads')
                .upload(`public/${photo.name}`, photo);

            if (error) {
                alert('Error uploading photo: ' + error.message);
                return;
            }
            photo_path = data.path;
        }

        const newObservation = {
            species_guess,
            common_name,
            description: notes,
            voyage_id: selectedVoyage,
            user_id: selectedUser,
            // photo_path: photo_path, // The backend does not support this yet
        };

        const response = await fetch('http://localhost:8004/observations', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newObservation)
        });

        if (response.ok) {
            alert('Observation created successfully!');
        } else {
            alert('Failed to create observation.');
        }
    }
</script>

<h1>Log New Observation</h1>

<form on:submit|preventDefault={handleSubmit}>
    <div>
        <label for="voyage">Voyage</label>
        <select id="voyage" bind:value={selectedVoyage} required>
            {#each voyages as voyage}
                <option value={voyage.voyage_id}>{voyage.name}</option>
            {/each}
        </select>
    </div>
    <div>
        <label for="user">User</label>
        <select id="user" bind:value={selectedUser} required>
            {#each users as user}
                <option value={user.user_id}>{user.username}</option>
            {/each}
        </select>
    </div>
    <div>
        <label for="species_guess">Species Guess</label>
        <input id="species_guess" type="text" bind:value={species_guess} />
    </div>
    <div>
        <label for="common_name">Common Name</label>
        <input id="common_name" type="text" bind:value={common_name} />
    </div>
    <div>
        <label for="notes">Notes</label>
        <textarea id="notes" bind:value={notes}></textarea>
    </div>
    <div>
        <label for="photo">Photo</label>
        <input id="photo" type="file" on:change={e => photo = e.target.files[0]} />
    </div>
    <button type="submit">Submit</button>
</form>
