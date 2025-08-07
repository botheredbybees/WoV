<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    let user = {};
    let userId = $page.params.id;

    onMount(async () => {
        const response = await fetch(`http://localhost:8004/users/${userId}`);
        user = await response.json();
    });

    async function handleSubmit() {
        const response = await fetch(`http://localhost:8004/users/${userId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(user)
        });

        if (response.ok) {
            alert('User updated successfully!');
        } else {
            alert('Failed to update user.');
        }
    }
</script>

<h1>Edit User</h1>

<form on:submit|preventDefault={handleSubmit}>
    <div>
        <label for="username">Username</label>
        <input id="username" type="text" bind:value={user.username} />
    </div>
    <div>
        <label for="email">Email</label>
        <input id="email" type="email" bind:value={user.email} />
    </div>
    <div>
        <label for="role">Role</label>
        <input id="role" type="text" bind:value={user.role} />
    </div>
    <button type="submit">Save</button>
</form>
