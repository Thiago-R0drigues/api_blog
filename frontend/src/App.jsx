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
    const data = await answer.json()
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
        <form onSubmit={sendForm}>
          <input
            type="text"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
            placeholder="Título"
          />

          <input
            type='text'
            value={content}
            onChange={(event) => setContent(event.target.value)}
            placeholder="Conteúdo"
          />

          <button type="submit">Enviar</button>
        </form>
      </section>

      <section>
        <h1 className='h-20 text-center pt-20 text-4xl font-mono'>POSTS</h1>
        {posts.map((post) => (
          <div key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.content}</p>
          </div>
        ))}
      </section>
    </>
  )
}

export default App
