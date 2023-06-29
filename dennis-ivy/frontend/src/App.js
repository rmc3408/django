import React from 'react'
import './App.css'
import Header from './components/Header'
import NotesListPage from './pages/NotesListPage'
import NotePage from './pages/NotePage'
import ErrorPage from './pages/error-page'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

const router = createBrowserRouter([
    {
        path: '/',
        element: <NotesListPage />,
        errorElement: <ErrorPage />,
    },
    {
        path: '/notes/:id',
        element: <NotePage />,
    },
])

function App() {
    return (
        <>
            <div className='container dark'>
                <div className='app'>
                    <Header />
                    <RouterProvider router={router} />
                </div>
            </div>
        </>
    )
}

export default App
