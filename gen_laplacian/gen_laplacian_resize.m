addpath matting/
addpath gaimc/
N = 60;

for i = 1:N
    i
    prefix = '../examples/input_resize/';
    in_name = [prefix 'in' int2str(i) '.png']; 
    input = im2double(imread(in_name));
    input = reshape_img(input, 700);
    size(input)  
    [h w c] = size(input);
    
    
    A = getLaplacian1(input, zeros(h, w), 1e-7, 1);
    n = nnz(A);
    [Ai, Aj, Aval] = find(A);
    CSC = [Ai, Aj, Aval];
    %save(['/home/wangyannhao/Github/671/deep-photo-styletransfer/gen_laplacian/matrix_resize/Input_Laplacian_3x3_1e-7_CSC' int2str(i) '.mat'], 'CSC');
    
    [rp ci ai] = sparse_to_csr(A);
    Ai = sort(Ai);
    Aj = ci;
    Aval = ai;
    CSR = [Ai, Aj, Aval];
    save(['/home/wangyannhao/Github/671/deep-photo-styletransfer/gen_laplacian/matrix_resize/Input_Laplacian_3x3_1e-7_CSR' int2str(i) '.mat'], 'CSR');
 
end 

exit