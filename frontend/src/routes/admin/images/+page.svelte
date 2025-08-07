<script>
    import { onMount } from 'svelte';
    import { supabase } from '$lib/supabaseClient';

    let images = [];

    onMount(async () => {
        const response = await fetch('http://localhost:8004/images');
        images = await response.json();
    });

    async function deleteImage(imageId, filePath) {
        if (confirm('Are you sure you want to delete this image?')) {
            const { error: storageError } = await supabase.storage
                .from('photo-uploads')
                .remove([filePath]);

            if (storageError) {
                alert('Error deleting image from storage: ' + storageError.message);
                return;
            }

            const response = await fetch(`http://localhost:8004/images/${imageId}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                images = images.filter(img => img.image_id !== imageId);
                alert('Image deleted successfully!');
            } else {
                alert('Failed to delete image from database.');
            }
        }
    }
</script>

<h1>Manage Images</h1>

<table>
    <thead>
        <tr>
            <th>Image</th>
            <th>File Path</th>
            <th>Observation ID</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {#each images as image}
            <tr>
                <td><img src="{supabase.storage.from('photo-uploads').getPublicUrl(image.file_path).data.publicUrl}" alt="observation" width="100" /></td>
                <td>{image.file_path}</td>
                <td>{image.observation_id}</td>
                <td>
                    <button on:click={() => deleteImage(image.image_id, image.file_path)}>Delete</button>
                </td>
            </tr>
        {/each}
    </tbody>
</table>
