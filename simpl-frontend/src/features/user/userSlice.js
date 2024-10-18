import { createSlice } from '@reduxjs/toolkit'

export const userSlice = createSlice({
    name: 'user',
    initialState: {
        value: null
    },
    reducers: {
        setUser: (state, action) => {
            state.value = action.payload
        },
        logout: (state) => {
            state.value = null
        },
        updateUser: (state, action) => {
            state.value = { ...state.value, ...action.payload }
        }
    }
})

export const { setUser, logout, updateUser } = userSlice.actions

export default userSlice.reducer