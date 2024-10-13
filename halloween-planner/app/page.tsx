"use client"

import React, { useState } from 'react'
import Image from 'next/image'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Skeleton } from "@/components/ui/skeleton"
import { Ghost, Users, MapPin, Cake, DollarSign, ShoppingCart } from "lucide-react"
import { Calendar } from "@/components/ui/calendar"

type FormData = {
  dates: string[]
  num_people: number
  interests: string[]
  location: string
  age: number
  budget: number
}

type Costume = {
  character: string
  description: string
}

type CostumeIdea = {
  costumes: Costume[]
  description: string
  theme: string
}

type Party = {
  date: string
  description: string
  location: string
  name: string
  time: string
}

type TripDay = {
  costume_idea: CostumeIdea
  date: string
  estimated_cost: number
  party: Party
}

type Itinerary = {
  trip: TripDay[]
}

function HalloweenForm({ onSubmit }: { onSubmit: (data: FormData) => void }) {
  const [formData, setFormData] = useState<FormData>({
    dates: [],
    num_people: 4,
    interests: [],
    location: '',
    age: 21,
    budget: 500
  })

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    console.log('Form submitted with data:', formData)
    onSubmit(formData)
  }

  const addInterest = (interest: string) => {
    if (interest && !formData.interests.includes(interest)) {
      setFormData(prevData => ({
        ...prevData,
        interests: [...prevData.interests, interest]
      }))
    }
  }

  const removeInterest = (interest: string) => {
    setFormData(prevData => ({
      ...prevData,
      interests: prevData.interests.filter(i => i !== interest)
    }))
  }

  return (
    <Card className="w-full max-w-4xl mx-auto shadow-lg">
      <CardHeader className="bg-orange-500 text-white rounded-t-lg">
        <CardTitle className="text-2xl font-bold">Plan Your Halloween Adventure</CardTitle>
        <CardDescription className="text-orange-100">Fill in the details for your spooky celebration!</CardDescription>
      </CardHeader>
      <CardContent className="p-6">
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <Label htmlFor="dates" className="flex items-center text-orange-700">
              <Ghost className="mr-2 h-4 w-4" />
              Select Halloween Dates
            </Label>
            <div className="flex justify-center">
              <Calendar
                mode="multiple"
                selected={formData.dates.map(dateString => {
                  const [year, month, day] = dateString.split('-').map(Number);
                  return new Date(year, month - 1, day);
                })}
                onSelect={(dates) => {
                  if (dates) {
                    const updatedDates = dates.map(d => {
                      const year = d.getFullYear();
                      const month = String(d.getMonth() + 1).padStart(2, '0');
                      const day = String(d.getDate()).padStart(2, '0');
                      return `${year}-${month}-${day}`;
                    });
                    setFormData(prevData => ({ ...prevData, dates: updatedDates }));
                  } else {
                    setFormData(prevData => ({ ...prevData, dates: [] }));
                  }
                }}
                className="rounded-md border mt-1"
                fromDate={new Date()}
                toDate={new Date(new Date().getFullYear(), 9, 31)}
              />
            </div>
          </div>
          <div>
            <Label htmlFor="num_people" className="flex items-center text-orange-700">
              <Users className="mr-2 h-4 w-4" />
              Number of people
            </Label>
            <Input
              id="num_people"
              type="number"
              value={formData.num_people}
              onChange={(e) => setFormData(prevData => ({ ...prevData, num_people: parseInt(e.target.value) || 0 }))}
              min="1"
              className="mt-1"
            />
          </div>
          <div>
            <Label htmlFor="interests" className="flex items-center text-orange-700">
              <Ghost className="mr-2 h-4 w-4" />
              Interests
            </Label>
            <div className="flex items-center space-x-2 mt-1">
              <Input
                id="interests"
                placeholder="Type an interest and press Enter"
                onKeyPress={(e: React.KeyboardEvent<HTMLInputElement>) => {
                  if (e.key === 'Enter') {
                    e.preventDefault()
                    addInterest((e.target as HTMLInputElement).value)
                    ;(e.target as HTMLInputElement).value = ''
                  }
                }}
              />
              <Button type="button" onClick={() => {
                const interestsInput = document.getElementById('interests') as HTMLInputElement;
                addInterest(interestsInput.value)
                interestsInput.value = ''
              }}>
                Add
              </Button>
            </div>
            <div className="mt-2 flex flex-wrap gap-2">
              {formData.interests.map((interest, index) => (
                <span key={index} className="bg-orange-200 text-orange-800 px-2 py-1 rounded-full text-sm flex items-center">
                  {interest}
                  <button onClick={() => removeInterest(interest)} className="ml-2 focus:outline-none">
                    <Ghost className="h-4 w-4" />
                  </button>
                </span>
              ))}
            </div>
          </div>
          <div>
            <Label htmlFor="location" className="flex items-center text-orange-700">
              <MapPin className="mr-2 h-4 w-4" />
              Location
            </Label>
            <Input
              id="location"
              value={formData.location}
              onChange={(e) => setFormData(prevData => ({ ...prevData, location: e.target.value }))}
              placeholder="e.g. University of Illinois at Urbana-Champaign"
              className="mt-1"
            />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <Label htmlFor="age" className="flex items-center text-orange-700">
                <Cake className="mr-2 h-4 w-4" />
                Age
              </Label>
              <Input
                id="age"
                type="number"
                value={formData.age}
                onChange={(e) => setFormData(prevData => ({ ...prevData, age: parseInt(e.target.value) || 0 }))}
                min="1"
                className="mt-1"
              />
            </div>
            <div>
              <Label htmlFor="budget" className="flex items-center text-orange-700">
                <DollarSign className="mr-2 h-4 w-4" />
                Budget
              </Label>
              <Input
                id="budget"
                type="number"
                value={formData.budget}
                onChange={(e) => setFormData(prevData => ({ ...prevData, budget: parseInt(e.target.value) || 0 }))}
                min="0"
                className="mt-1"
              />
            </div>
          </div>
          <Button 
            type="submit" 
            className="w-full bg-orange-500 hover:bg-orange-600 text-white"
            onClick={() => console.log('Current form data:', formData)}
          >
            Plan My Halloween
          </Button>
        </form>
      </CardContent>
    </Card>
  )
}

function LoadingPage() {
  return (
    <div className="flex flex-col items-center justify-center space-y-4">
      <Ghost className="w-16 h-16 text-orange-600 animate-bounce" />
      <div className="text-2xl font-bold text-orange-600">Summoning your spooky plans...</div>
      <Skeleton className="w-[250px] h-[20px] rounded-full" />
      <Skeleton className="w-[200px] h-[20px] rounded-full" />
      <Skeleton className="w-[300px] h-[20px] rounded-full" />
    </div>
  )
}

function ResultsPage({ results }: { results: Itinerary }) {
  return (
    <div className="space-y-8">
      <h2 className="text-2xl font-bold text-orange-600 mb-6">Halloween Party Results</h2>
      {results.trip.map((tripDay, index) => (
        <Card key={index} className="mb-8 bg-orange-50 hover:shadow-lg transition-shadow duration-300">
          <CardHeader className="bg-orange-200">
            <CardTitle className="text-2xl text-orange-800">{tripDay.party.name}</CardTitle>
            <CardDescription className="text-lg text-orange-700">
              {new Date(tripDay.date).toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })} - {tripDay.party.time}
            </CardDescription>
          </CardHeader>
          <CardContent className="p-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="space-y-4">
                <h4 className="text-xl font-bold text-orange-700 mb-4">Event Details</h4>
                <p><strong className="text-orange-600">Location:</strong> {tripDay.party.location}</p>
                <p><strong className="text-orange-600">Description:</strong> {tripDay.party.description}</p>
              </div>
              <div className="space-y-4">
                <h4 className="text-xl font-bold text-orange-700 mb-4">Suggested Group Costume: {tripDay.costume_idea.theme}</h4>
                <p><strong className="text-orange-600">Description:</strong> {tripDay.costume_idea.description}</p>
                <div className="space-y-2">
                  {tripDay.costume_idea.costumes.map((costume, costumeIndex) => (
                    <div key={costumeIndex} className="bg-white p-4 rounded-lg shadow-md">
                      <h5 className="text-lg font-semibold text-orange-600 mb-2">{costume.character}</h5>
                      <p className="text-sm text-gray-600 mb-4">{costume.description}</p>
                    </div>
                  ))}
                </div>
                <p className="mt-4 font-semibold text-orange-700">Estimated Cost: ${tripDay.estimated_cost.toFixed(2)}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}

export default function HalloweenPlanner() {
  const [stage, setStage] = useState<'form' | 'loading' | 'results'>('form')
  const [formData, setFormData] = useState<FormData | null>(null)
  const [results, setResults] = useState<Itinerary | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleFormSubmit = async (data: FormData) => {
    setFormData(data)
    setStage('loading')
    setError(null)

    console.log('Submitting data to API:', data)

    try {
      const response = await fetch('http://localhost:3002/plan-halloween', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })

      if (!response.ok) {
        throw new Error('Failed to fetch Halloween plans')
      }

      // Log the raw response text
      const rawResponseText = await response.text()
      console.log('Raw API response:', rawResponseText)

      // Parse the response text into JSON
      let halloweenResults: any
      try {
        halloweenResults = JSON.parse(rawResponseText)
      } catch (parseError) {
        console.error('Error parsing JSON:', parseError)
        throw new Error('Invalid JSON response from API')
      }

      console.log('Parsed API response:', halloweenResults)

      // Log specific parts of the response
      console.log('Trip:', halloweenResults.json_dict.trip)

      // Set results to the json_dict which contains the trip data
      setResults(halloweenResults.json_dict)
      setStage('results')
    } catch (error) {
      console.error('Error:', error)
      setError('An error occurred while planning your Halloween adventure. Please try again.')
      setStage('form')
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-orange-100 to-orange-200">
      <header className="bg-orange-600 text-white p-4">
        <h1 className="text-2xl font-bold">🎃 Spooky Halloween Planner</h1>
      </header>
      <main className="container mx-auto p-4">
        {stage === 'form' && <HalloweenForm onSubmit={handleFormSubmit} />}
        {stage === 'loading' && <LoadingPage />}
        {stage === 'results' && results && <ResultsPage results={results} />}
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <strong  className="font-bold">Error: </strong>
            <span className="block sm:inline">{error}</span>
          </div>
        )}
      </main>
    </div>
  )
}
