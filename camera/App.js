import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView, Button, Image } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera, CameraType} from 'expo-camera';
import { shareAsync } from 'expo-sharing';
import * as MediaLibrary from 'expo-media-library';

export default function App() {
  let cameraRef = useRef();
  const [hasCameraPermission, setHasCameraPermission] = useState();
  const [hasMediaLibraryPermission, setHasMediaLibraryPermission] = useState();
  const [photo, setPhoto] = useState();
  const [type, setType] = useState(CameraType.back);
  const [backPhoto, setBackPhoto] = useState();
  const [backPhotoReady, setBackPhotoReady] = useState(false);

  useEffect(() => {
    (async () => {
      const cameraPermission = await Camera.requestCameraPermissionsAsync();
      const mediaLibraryPermission = await MediaLibrary.requestPermissionsAsync();
      setHasCameraPermission(cameraPermission.status === "granted");
      setHasMediaLibraryPermission(mediaLibraryPermission.status === "granted");
    })();
  }, []);

  if (hasCameraPermission === undefined) {
    return <Text>Requesting permissions...</Text>
  } else if (!hasCameraPermission) {
    return <Text>Permission for camera not granted. Please change this in settings.</Text>
  }

  let takePic = async () => {
    let options = {
      quality: 1,
      base64: true,
      exif: false
    };
    if (!photo) {
      let newPhoto = await cameraRef.current.takePictureAsync(options);
      toggleCameraType();
      setPhoto(newPhoto);
      //takePic();
    }
    else if (!backPhoto) {
      let otherPhoto = await cameraRef.current.takePictureAsync(options);
      setBackPhoto(otherPhoto);
    }
    
    
  };

  if (photo && backPhoto) {
    let sharePic = () => {
      shareAsync(photo.uri).then(() => {
        setPhoto(undefined);
      });
    };

    let savePhoto = () => {
      MediaLibrary.saveToLibraryAsync(photo.uri).then(() => {
        setPhoto(undefined);
      });
    };
    
    return (
      <SafeAreaView style={styles.container}>
        <Image style={styles.preview} source={{ uri: "data:image/jpg;base64," + photo.base64 }} />
        <Image style={styles.preview} source={{ uri: "data:image/jpg;base64," + backPhoto.base64 }} />
        <Button title="Share" onPress={sharePic} />
        {hasMediaLibraryPermission ? <Button title="Save" onPress={savePhoto} /> : undefined}
        <Button title="Discard" onPress={() => setPhoto(undefined)} />
      </SafeAreaView>
    );
  }
  function toggleCameraType() {
    setType(current => (current === CameraType.back ? CameraType.front : CameraType.back));
  }
  let takeBackPhoto= async () => {
    let options = {
      quality: 1,
      base64: true,
      exif: false
    };
    if (!backPhoto && photo) {
      let otherPhoto = await cameraRef.current.takePictureAsync(options);
      setBackPhoto(otherPhoto);
    }
  }
  
  return (
    <Camera style={styles.container} ref={cameraRef} type={type} onCameraReady={takeBackPhoto} >
      <View style={styles.buttonContainer}>
        <Button title="Take Pic" onPress={takePic} />
        <Button title="Reverse" onPress={toggleCameraType}/>
      </View>
      <StatusBar style="auto" />
    </Camera>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttonContainer: {
    backgroundColor: '#fff',
    alignSelf: 'flex-end'
  },
  preview: {
    alignSelf: 'stretch',
    flex: 1
  }
});