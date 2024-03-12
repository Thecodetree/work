async function fetchData() {
    try { const response = 
        await fetch('https://api.example.com/data');
        const data = await response.json();
        console.log(data);
        return data;}
        catch (error) {
            console.error('There has been an error fetching the data:',
            error);
        }
}

fetchData();