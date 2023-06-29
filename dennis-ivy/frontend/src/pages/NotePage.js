import React, { useState, useEffect } from 'react'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
import { useParams, useNavigate } from 'react-router-dom'

const BASE_URL = 'http://localhost:4000/api'

const NotePage = () => {
    let { id: noteId } = useParams()
    const navigate = useNavigate()
    let [note, setNote] = useState(null)

    useEffect(() => {
        getNote()
    }, [noteId])

    let getNote = async () => {
        if (noteId === 'new') return

        let response = await fetch(`${BASE_URL}/notes/${noteId}`)
        let data = await response.json()
        setNote(data)
    }

    let createNote = async () => {
        fetch(`${BASE_URL}/notes/create`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(note),
        })
        navigate(-1)
    }

    let updateNote = async () => {
        fetch(`${BASE_URL}/notes/update/${noteId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(note),
        })
        navigate(-1)
    }

    let deleteNote = async () => {
        fetch(`${BASE_URL}/notes/delete/${noteId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        navigate(-1)
    }

    let handleChange = (value) => {
        setNote((note) => ({ ...note, body: value }))
    }

    return (
        <div className='note'>
            <div className='note-header'>
                <h3>
                    <ArrowLeft onClick={() => navigate(-1)} />
                </h3>
                {noteId == 'new' ? (
                    <button onClick={createNote} disabled={note?.body == ''}>
                        Done
                    </button>
                ) : (
                    <div>
                        <button onClick={deleteNote}>Delete</button>
                        <button onClick={updateNote}>Update</button>
                    </div>
                )}
            </div>
            <textarea
                onChange={(e) => {
                    handleChange(e.target.value)
                }}
                value={note?.body}
            ></textarea>
        </div>
    )
}

export default NotePage
