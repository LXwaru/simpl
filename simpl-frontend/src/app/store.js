import {configureStore} from '@reduxjs/toolkit';
import storage from 'redux-persist/lib/storage'
import {combineReducers} from "redux"; 
import { persistReducer, persistStore } from 'redux-persist'
import { thunk } from 'redux-thunk';
import userSlice from '../features/user/userSlice';

const reducers = combineReducers({
    user: userSlice
});

const persistConfig = {
    key: 'root',
    storage
};

const persistedReducer = persistReducer(persistConfig, reducers);


const store = configureStore({
    reducer: persistedReducer,
    devTools: process.env.NODE_ENV !== 'production',
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            serializableCheck: false, // This avoids errors with non-serializable data in the state
        }).concat(thunk), // Adds thunk middleware
});

export const persistor = persistStore(store);

export default store;