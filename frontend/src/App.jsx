import { useState, useEffect } from 'react';

function App() {
  //pega os posts
  const [posts, setPosts] = useState([])

  //cria posts
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  async function sendForm(event) {
    event.preventDefault();

    const answer = await fetch('http://localhost:8000/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        post_title: title,
        post_description: content
      }),
    });


    if (answer.ok) {
      const newPost = await answer.json()
      setPosts((currentPosts) => [newPost, ...currentPosts]);

      setTitle('');
      setContent('');
    }

    
  }


  useEffect(() => {
    fetch("http://localhost:8000/posts")
      .then((response) => response.json())
      .then((data) => {
        setPosts(data);
      })
      .catch((error) => {
        console.error("Erro:", error);
      });
  }, []);

  console.log(posts)

  return (
    <>
      <section>
        <div className='flex justify-around border h-10 items-center bg-gray-500'>
          <p className='text-2xl font-serif hover:cursor-pointer'>BLOG!</p>
          <button className='hover:cursor-pointer hover:text-white'>Log In</button>
        </div>
      </section>

      <section>
          <form onSubmit={sendForm} className='flex flex-col w-100 border'>
            <input
              type="text"
              value={title}
              onChange={(event) => setTitle(event.target.value)}
              placeholder="Título"
              className='text-center'
            />

            <input
              type='text'
              value={content}
              onChange={(event) => setContent(event.target.value)}
              placeholder="Conteúdo"
              className='text-center'
            />

            <button type="submit" className='bg-gray-600 w-40 m-auto p-1 mb-3 mt-3'>Enviar</button>
          </form>
      </section>

      <section>
        <h1 className='h-20 text-center pt-20 text-4xl font-mono'>POSTS</h1>
        {posts.map((post) => (
          <ul>
            <li key={post.id}>
              <p>{post.post_title}</p>
              <p>{post.post_description}</p>
            </li>
          </ul>
        ))}
      </section>
    </>
  )
}

export default App
