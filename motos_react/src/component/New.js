import React from 'react'
import { useParams } from 'react-router'

export default function New() {
    const params = useParams()
  return (
    <h1>{params.newsId}</h1>
  )
}
